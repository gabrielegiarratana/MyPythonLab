import sys, getopt

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print(f"{sys.argv[0]} -i <inputfile> -o <outputfile>'")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print
            'date_test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print (f"Input file is '{inputfile}', Output file is '{outputfile}'")