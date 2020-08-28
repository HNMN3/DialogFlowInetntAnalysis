import csv
import sys
import uuid
from time import sleep

import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument
from tqdm import trange

from constants import (OUTPUT_FILE, DIALOGFLOW_PROJECT_ID,
                       DIALOGFLOW_LANGUAGE_CODE)


def read_file(file_name):
    try:
        f_obj = open(file_name)
        reader = csv.reader(f_obj)
        # Skip header
        next(reader)
        question_phrases = list()
        for line in reader:
            input_phrase = line[0]
            question_phrases.append(input_phrase.strip())
        return question_phrases
    except FileNotFoundError:
        print("No file found with name: {}".format(file_name))
    except Exception as err:
        print("Unable to open the file due to error: {}".format(err))
    # Quit the program if any file reading is not successful
    quit()


def call_the_api(input_phrase, session_id):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=input_phrase,
                                            language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    result = [input_phrase, response.query_result.fulfillment_text,
              response.query_result.intent.display_name,
              response.query_result.intent_detection_confidence]
    return result


def write_to_file(output_row, output_file):
    with open(output_file, 'a') as f_obj:
        writer = csv.writer(f_obj)
        writer.writerow(output_row)


def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py INPUT_FILE_PATH")
        quit()
    input_file = arguments[1]
    input_phrases = read_file(input_file)
    input_phrases_len = len(input_phrases)
    session_id = str(uuid.uuid4())
    output_file_name = OUTPUT_FILE.format(session_id)
    header = ["Input Phrase", "Dialogflow Response", "Matched Intent(s)", "Confidence"]
    write_to_file(header, output_file_name)

    for i in trange(input_phrases_len, file=sys.stdout, desc='DialogFlow API Calls'):
        input_phrase = input_phrases[i]
        try:
            output = call_the_api(input_phrase, session_id)
        except Exception as err:
            output = [input_phrase, "Unable to get output due to err: {}".format(err)]

        write_to_file(output, output_file_name)
        sleep(1)

    print("Output stored to file: {}".format(output_file_name))


if __name__ == '__main__':
    main()
