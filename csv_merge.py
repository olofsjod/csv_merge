# csv_merge.py
# written by Olof Sjödin <olsj@kth.se> 2024-05-06

import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="This merges many csv files and sort them.")

    parser.add_argument(
        "csv_filenames", metavar="csv_file", type=str, nargs="+", help="The files which will be merged and sort them."
    )
    parser.add_argument(
        "--col", type=int, help="The column number which the sorting will be based on. Default: 1.", default=1
    )
    parser.add_argument(
        "--delimiter", type=str, help="The delimiter in CSV file. Default: ',' ", default=","
    )
    parser.add_argument(
        "--outfile", type=str, default="out.csv"
    )

    args = parser.parse_args()

    data_mxs = []
    for csv_filename in args.csv_filenames:
        data_mx = np.genfromtxt(csv_filename, delimiter=args.delimiter)
        data_mxs.append(data_mx)

    data_mxs_merged = np.vstack((*data_mxs, ))

    # Sort matrix with respect to column n
    data_mxs_merged = data_mxs_merged[data_mxs_merged[:, args.col-1].argsort()]

    np.savetxt(args.outfile, data_mxs_merged, delimiter=args.delimiter)


if __name__ == "__main__":
    main()
