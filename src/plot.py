import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def setup_plot(figsize=(10, 5)):
    plt.figure(figsize=figsize)


def plot_histogram(
    df: pd.DataFrame,
    column: str,
    bins: int,
    title: str,
    xlabel: str,
    ylabel: str = "Customers"
):

    setup_plot()

    sns.histplot(
        data=df,
        x=column,
        bins=bins
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()


def plot_line(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    xlabel: str,
    ylabel: str,
    figsize=(10, 5)
):

    setup_plot(figsize)

    sns.lineplot(
        data=df,
        x=x,
        y=y,
        marker="o"
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()


def plot_box(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    xlabel: str,
    ylabel: str,
    figsize=(10, 5)
):

    setup_plot(figsize)

    sns.boxplot(
        data=df,
        x=x,
        y=y
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()


def plot_scatter(
    df: pd.DataFrame,
    x: str,
    y: str,
    hue: str,
    title: str,
    xlabel: str,
    ylabel: str,
    figsize=(10, 6),
    alpha=0.3
):

    setup_plot(figsize)

    sns.scatterplot(
        data=df,
        x=x,
        y=y,
        hue=hue,
        alpha=alpha
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()


def plot_bar(
    df,
    x,
    y,
    title,
    xlabel,
    ylabel,
    figsize=(10, 5)
):
    setup_plot(figsize)

    sns.barplot(
        data=df,
        x=x,
        y=y
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()


def plot_heatmap(
    df,
    title,
    xlabel,
    ylabel,
    figsize=(10, 6),
    annot=True,
    fmt=".1f",
    cmap="RdYlGn_r"
):

    setup_plot(figsize)

    sns.heatmap(
        df,
        annot=annot,
        fmt=fmt,
        cmap=cmap
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()