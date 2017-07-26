import argparse
import io

from google.cloud import speech
speech_client = speech.Client()

def transcribe_speech_sync(speech_file):
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()
        audio_sample = speech_client.sample(
            content=content,
            source_uri=None,
            encoding='LINEAR16',
            sample_rate_hertz=16000)

    alternatives = audio_sample.recognize('en-US')
    for alternative in alternatives:
        print('Transcript: {}, Confidence: {}'.format(alternative.transcript, alternative.confidence))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for audio file to be recognized')

    args = parser.parse_args()
    transcribe_speech_sync(args.path)
