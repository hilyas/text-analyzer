import click
from text_analyzer import TextStatistics, TextNLP
from text_scraper import TextScraper, WebRequester

def read_content_from_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def get_content_from_source(source, source_type):
    """Retrieve content based on the source type (URL or file)"""
    if source_type == "url":
        requester = WebRequester()
        scraper = TextScraper(requester)
        return scraper.scrape_website(url=source)
    else:  # source_type == "file"
        return read_content_from_file(source)

def perform_text_analysis(content):
    """Analyze text and return the stats"""
    text_statistics = TextStatistics(content=content)
    return text_statistics.analyze_text()

def perform_sentiment_analysis(content):
    """Perform sentiment analysis and return the sentiment"""
    text_nlp = TextNLP(content=content)
    return text_nlp.get_sentiment()

def display_text_analysis(total, word_freq, avg_word_length, letter_freq, total_sentences, type, top):
    """Display the text analysis results"""
    click.echo(f"Total words: {total}")
    click.echo(f"Average word length: {avg_word_length:.2f}")
    click.echo(f"Total sentences: {total_sentences}")

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

@click.group()
def main():
    """Advanced CLI for textual analysis of scraped content."""
    pass

@main.command()
@click.argument(
    "source", 
    required=True, 
    type=str) 
@click.option(
    "--source-type", 
    type=click.Choice(["url", "file"]), 
    default="url", 
    help="Specify if the source is a URL or file path.")
@click.option(
    "--top",
    multiple=True,
    type=int,
    default=[5],
    help="Multiple top counts e.g. --top 5 --top 10",
)
@click.option(
    "--type",
    type=click.Choice(["words", "letters", "both"]),
    default="both",
    help="Type of analysis.",
)
@click.option(
    "--verbose",
    is_flag=True,
    help="Verbose mode: print more data."
)
def analyze(top, source, source_type, type, verbose):
    """Main analyze method that orchestrates the various functions"""
    content = get_content_from_source(source, source_type)

    if not content:
        click.echo(f"Failed to retrieve content from {source}.")
        return

    try:
        total, word_freq, avg_word_length, letter_freq, total_sentences = perform_text_analysis(content)
        display_text_analysis(total, word_freq, avg_word_length, letter_freq, total_sentences, type, top)
    except Exception as e:
        click.echo(f"An error occurred during analysis: {e}")
        return

    try:
        sentiment = perform_sentiment_analysis(content)
        sentiment_output = f"Sentiment: neg={sentiment['neg']:.3f}, " \
                       f"neu={sentiment['neu']:.3f}, " \
                       f"pos={sentiment['pos']:.3f}, " \
                       f"compound={sentiment['compound']:.4f}"
        click.echo(sentiment_output)
    except Exception as e:
        click.echo(f"An error occurred during sentiment analysis: {e}")
        return

    if verbose:
        click.echo("\nVerbose Mode:")
        click.echo(f"Source analyzed: {source}")
        click.echo(f"Total unique words: {len(word_freq)}")
        click.echo(f"Total unique letters: {len(letter_freq)}")

if __name__ == "__main__":
    main()
