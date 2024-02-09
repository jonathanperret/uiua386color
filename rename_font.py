import sys
from fontTools import ttLib

def main(_, infile, newname, outfile):
    font = ttLib.TTFont(infile)

    nametable = font["name"]

    for record in nametable.names:
        original = record.toUnicode()
        if "Uiua386" in original:
            newstring = original.replace("Uiua386", newname)
            print("Replacing {} with {}".format(original, newstring))
            record.string = newstring

    print("Saving to {}".format(outfile))
    font.save(outfile)
    font.close()

if __name__ == "__main__":
    main(*sys.argv)
