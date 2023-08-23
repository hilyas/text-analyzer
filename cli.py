import click
from text_analyzer import TextAnalyzer
from text_scraper import TextScraper

@click.group()
def main():
    """Advanced CLI for textual analysis of scraped content."""
    pass

@main.command()
@click.option("--url", prompt=True, help="URL to analyze.")
@click.option(
    "--top",
    multiple=True,
    type=int,
    default=[10],
    help="Multiple top counts e.g. --top 5 --top 10",
)
@click.option(
    "--type",
    type=click.Choice(["words", "letters", "both"]),
    default="both",
    help="Type of analysis.",
)
@click.option("--verbose", is_flag=True, help="Verbose mode: print more data.")
def analyze(url, top, type, verbose):
    scraper = TextScraper()
    content = scraper.scrape_website(url=url)
    analyzer = TextAnalyzer(content=content)
    total, word_freq, avg_word_length, letter_freq, total_sentences, sentiment = analyzer.analyze_text()

    click.echo(f"Total words: {total}")
    click.echo(f"Average word length: {avg_word_length:.2f}")
    click.echo(f"Total sentences: {total_sentences}")
    sentiment_output = f"Sentiment: neg={sentiment['neg']:.3f}, " \
                   f"neu={sentiment['neu']:.3f}, " \
                   f"pos={sentiment['pos']:.3f}, " \
                   f"compound={sentiment['compound']:.4f}"
    click.echo(sentiment_output)

    if type in ["words", "both"]:
        for top_count in top:
            click.echo(f"\nTop {top_count} frequent words:")
            for word, freq in word_freq.most_common(top_count):
                click.echo(f"{word}: {freq}")

    if type in ["letters", "both"]:
        for top_count in top:
            click.echo(f"\nTop {top_count} frequent letters:")
            for letter, freq in letter_freq.most_common(top_count):
                click.echo(f"{letter}: {freq}")

    if verbose:
        click.echo("\nVerbose Mode:")
        click.echo(f"URL analyzed: {url}")
        click.echo(f"Total unique words: {len(word_freq)}")
        click.echo(f"Total unique letters: {len(letter_freq)}")

if __name__ == "__main__":
    main()
