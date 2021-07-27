from json import dump, load

# import math
import numpy as np
import pandas as pd

from .evaluate import evaluate


def plot(
    function,
    title=None,
    left_domain=-10,
    right_domain=10,
    points=100,
    upper_limit=10,
    lower_limit=None,
    vertical_asymptote=[],
    horizontal_asymptote=[],
    oblique_asymptote=[],
    point=[],
    pretty=False,
):
    """Plot function with given configuration"""
    # Initialize lower limit
    lower_limit = -upper_limit if lower_limit is None else lower_limit
    # Create domain list
    xes = np.linspace(left_domain, right_domain, points)
    # Create image list
    yes = get_images(function, xes, upper_limit, lower_limit, pretty)
    # Create graph
    graph = pd.DataFrame(yes, xes)
    # Plot graph
    plt = graph.plot(kind="line", grid=True, title=title)
    # Plot X axis
    draw_axis(plt.hlines, left_domain, right_domain, lower_limit, upper_limit)
    # Plot Y axis
    draw_axis(plt.vlines, lower_limit, upper_limit, left_domain, right_domain)
    # Plot vertical asymptotes
    draw_vh_asymptotes(
        plt.vlines,
        vertical_asymptote,
        lower_limit,
        upper_limit
    )
    # Plot horizontal asymptotes
    draw_vh_asymptotes(
        plt.hlines,
        horizontal_asymptote,
        left_domain,
        right_domain
     )
    # Plot oblique asymptotes
    draw_oblique_asymptotes(
        plt,
        oblique_asymptote,
        left_domain,
        right_domain,
        lower_limit,
        upper_limit
    )
    # Draw points
    draw_points(plt, point)
    # Return plot object
    return plt


def draw_axis(axis, axis_min, axis_max, minimum, maximum):
    """Use function axis to plot the horizontal or vertical axis"""
    if minimum <= 0 and maximum >= 0:
        axis(0, axis_min, axis_max, color="k")


def affine_fn(x, slope, intercept):
    return x * slope + intercept


def inverse_affine_fn(y, slope, intercept):
    return (y - intercept) / slope


def bound_asymptote(slope, intercept, xmin, xmax, ymin, ymax):
    """Find the correct bounding box of a line with slope and intercept"""
    y_xmin = affine_fn(xmin, slope, intercept)
    if y_xmin > ymax:
        return bound_asymptote(
            slope,
            intercept,
            inverse_affine_fn(ymax, slope, intercept),
            xmax,
            ymin,
            ymax,
        )
    if y_xmin < ymin:
        return bound_asymptote(
            slope,
            intercept,
            inverse_affine_fn(ymin, slope, intercept),
            xmax,
            ymin,
            ymax,
        )
    y_xmax = affine_fn(xmax, slope, intercept)
    if y_xmax < ymin:
        return bound_asymptote(
            slope,
            intercept,
            xmin,
            inverse_affine_fn(ymin, slope, intercept),
            ymin,
            ymax,
        )
    if y_xmax > ymax:
        return bound_asymptote(
            slope,
            intercept,
            xmin,
            inverse_affine_fn(ymax, slope, intercept),
            ymin,
            ymax,
        )
    return xmin, xmax, y_xmin, y_xmax


def draw_oblique_asymptotes(
    plt, oblique_asymptote, left_domain, right_domain, lower_limit, upper_limit
):
    if oblique_asymptote:
        for slope, intercept in oblique_asymptote:
            x1, x2, y1, y2 = bound_asymptote(
                slope,
                intercept,
                left_domain,
                right_domain,
                lower_limit,
                upper_limit
            )
            plt.plot([x1, x2], [y1, y2], color="gray", linestyle="dotted")


def draw_vh_asymptotes(asymptote, coord, minimum, maximum):
    """Plot horizontal and vertical asymptotes"""
    if coord:
        for c in coord:
            asymptote(coord, minimum, maximum,
                      color="gray", linestyles="dotted")


def draw_points(plt, points):
    if points:
        for x, y in points:
            draw_point(plt, x, y)


def draw_point(plt, x, y):
    plt.plot(x, y, color="gray", marker="o", markersize=3)


def save_figure(filename, plot):
    """Export the graph into filename"""
    if filename:
        plot_figure = plot.get_figure()
        plot_figure.savefig(filename)


def load_config(input_file):
    """Loads config from json file"""
    if input_file is not None:
        with open(input_file, "r") as fp:
            # Load from file
            return load(fp)
            # # Define deprecated keys
            # deprecated = []
            # # Load from file and remove deprecated keys
            # return {key: val for key, val in load(fp).items() if key not in deprecated}
    else:
        return {}


def store_config(output_file, config):
    """Stores config to json file"""
    if output_file is not None:
        with open(output_file, "w") as fp:
            # Removes None(s)
            dump(
                {key: val for key, val in config.items() if val is not None},
                fp,
            )


def update_config(from_cli, from_file):
    """Merge the two given dictionaries
    Updates the first dict with items from second if they're not already
    defined"""
    from_cli.update(
        {
            key: val
            for key, val in from_file.items()
            # Keep item if it is not already defined
            if key not in from_cli or from_cli[key] is None
        }
    )


def get_images(functions, domain, upper_limit, lower_limit, pretty=False):
    """Create a dict with functions images"""

    return {
        prettify(func, pretty): get_image(
            func,
            domain,
            upper_limit,
            lower_limit,
        )
        for func in functions
    }


def prettify(formula, pretty=False):
    if pretty:
        return formula.replace("(x)", "x").replace("**", "^")
    return formula


def get_image(func, domain, upper_limit, lower_limit):
    """For each x in domain, evaluate func"""
    return [evaluate(func, x, upper_limit, lower_limit) for x in domain]
