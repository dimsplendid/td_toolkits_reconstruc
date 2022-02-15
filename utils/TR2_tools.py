import pandas as pd


def tr2_score(column, method='mean', cmp='gt', scale=1., formatter=None):
    """
    Calculate the score base on the data.

    Parameters
    ----------
    column: numpy.array
    method: str, optional, default 'mean'
        'mean': Mean Normalization: score = (x - mean) / stdev
        'min-max': Min-Max Normalization: score = (x - min) / (max - min)
    cmp: str, optional, default 'gt'
        'gt': larger the better
        'lt': smaller the better
    scale: float, optional, default 1
        Scale the score by multiply.
    formatter: one parameter function, optional, default None
        Modified final score, like round to integer

    Returns
    -------
    numpy.array
    """
    if len(column) == 1:
        score = 0

    if method == 'mean':
        # Mean Normalization
        stdev = column.std()
        mean = column.mean()
        score = (column - mean) / stdev
        if cmp == 'lt':
            score = -score

    if method == 'min-max':
        # Min-Max Normalization
        min = column.min()
        max = column.max()
        if cmp == 'gt':
            score = (column - min) / (max - min)
        else:
            score = (max - column) / (max - min)

    score *= scale
    if formatter:
        score = formatter(score)

    return score
