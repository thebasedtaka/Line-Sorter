import argparse, re

#File sort logic
def sort_file(input): 
    try:
        with open(input, "r") as file:
            data = file.read()
            clean_sentences = []
            lines = data.splitlines()
            #Clear the white space and blank lines
            for s in lines:
                strip = s.strip()
                if re.search(r'[^\x00-\x7F]', s) or re.fullmatch(r'-+', s):
                    continue
                elif strip: 
                    clean_sentences.append(strip)
            #sort the sentences and ignore " characters
            sentences_sorted = sorted(clean_sentences, key=lambda s: s.strip('"').lower())
        return sentences_sorted
    except FileNotFoundError:
        print(f"Error: The file '{input}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#print file logic
def print_file(sentence_list, output_location, output_mode):
        #print to file
        if (output_mode == "file"):
            with open(output_location, "w") as outfile:
                for s in sentence_list:
                    outfile.write(s + "\n")
        #print to console
        else:
            for s in sentence_list:
                print(s)

if __name__ == "__main__":
    #Take console inputs
    parser = argparse.ArgumentParser(description='Sort lines in a text file, removing non-ASCII and dash-only lines',formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""Examples: %(prog)s input.txt %(prog)s input.txt -o output.txt %(prog)s input.txt -p console""")
    parser.add_argument("input_file", help="Input text file to process")
    parser.add_argument("-o", "--output", default='sorted.txt', help="Output file name (default: %(default)s)")
    parser.add_argument("-p", "--print", choices=['file', 'console'], default='file', help="Output destination (default: %(default)s)")
    
    #parse console input and run program 
    args = parser.parse_args()
    sentences = sort_file(args.input_file)

    print_file(sentences, args.output, args.print)