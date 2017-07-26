import argparse

from google.cloud import vision
vision_client = vision.Client()

def detect_labels(uri):
    image = vision_client.image(source_uri=uri)
    labels = image.detect_labels()

    print('Labels:')
    for label in labels:
        print(label.description)

def detect_faces(uri):
    image = vision_client.image(source_uri=uri)
    faces = image.detect_faces()

    print('Faces:')
    for face in faces:
        print('anger: {}'.format(face.emotions.anger))
        print('joy: {}'.format(face.emotions.joy))
        print('surprise: {}'.format(face.emotions.surprise))

        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in face.bounds.vertices])

        print('face bounds: {}'.format(','.join(vertices)))

def detect_text(uri):
    image = vision_client.image(source_uri=uri)
    texts = image.detect_text()

    print('Texts:')
    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in text.bounds.vertices])

        print('bounds: {}'.format(','.join(vertices)))

def detect_logos(uri):
    image = vision_client.image(source_uri=uri)
    logos = image.detect_logos()

    print('Logos:')
    for logo in logos:
        print(logo.description)

def run_uri(args):
    if args.command == 'labels-uri':
        detect_labels(args.uri)
    elif args.command == 'faces-uri':
        detect_faces(args.uri)
    elif args.command == 'text-uri':
        detect_text(args.uri)
    elif args.command == 'logos-uri':
        detect_logos(args.uri)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    labels_file_parser = subparsers.add_parser(
        'labels-uri', help=detect_labels.__doc__)
    labels_file_parser.add_argument('uri')

    faces_file_parser = subparsers.add_parser(
        'faces-uri', help=detect_faces.__doc__)
    faces_file_parser.add_argument('uri')

    text_file_parser = subparsers.add_parser(
        'text-uri', help=detect_text.__doc__)
    text_file_parser.add_argument('uri')

    logos_file_parser = subparsers.add_parser(
        'logos-uri', help=detect_logos_uri.__doc__)
    logos_file_parser.add_argument('uri')

    args = parser.parse_args()
    run_uri(args)