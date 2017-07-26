import argparse

from google.cloud import language
language_client = language.Client()

def print_sentiment_analysis(annotations):
    score = annotations.sentiment.score
    magnitude = annotations.sentiment.magnitude
    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0

    print('Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def detect_sentiment(movie_review_filename):
    with open(movie_review_filename, 'r') as review_file:
        document = language_client.document_from_html(review_file.read())

        annotations = document.annotate_text(include_sentiment=True,
                                             include_syntax=False,
                                             include_entities=False)

        print_sentiment_analysis(annotations)

def print_entities_analysis(annotations):
    for index, entity in enumerate(annotations.entities):
        entity_name = entity.name
        entity_salience = entity.salience
        print('Entity: {}, name: {}, salience: {}'.format(
            index, entity_name, entity_salience))

def detect_entities(text_snippet_filename):
    with open(text_snippet_filename, 'r') as snippet_file:
        document = language_client.document_from_html(snippet_file.read())

        annotations = document.annotate_text(include_sentiment=False,
                                            include_syntax=False,
                                            include_entities=True)

        print_entities_analysis(annotations)

def run_local(args):
    if args.command == 'sentiment':
        detect_sentiment(args.path)
    elif args.command == 'entities':
        detect_entities(args.path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    detect_sentiment_parser = subparsers.add_parser(
        'sentiment', help=detect_sentiment.__doc__)
    detect_sentiment_parser.add_argument('path')

    detect_entities_parser = subparsers.add_parser(
        'entities', help=detect_entities.__doc__)
    detect_entities_parser.add_argument('path')

    args = parser.parse_args()
    run_local(args)
