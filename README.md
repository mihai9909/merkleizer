# Merkleizer - README
The Merkleizer is a Python script that splits a file into chunks (100 chunks by default) and builds a Merkle tree from these chunks. It can be used to verify the integrity of a file (most likely you are better off using sha256sum) or see what chunks differ in files of the same size (use ```git diff``` instead :smile:).

## Requirements
Python 3.x

## Usage
```
usage: ./merkleize [-dc DEEP_COMPARE] [-c COMPARE] [-p PRETTY_PRINT] [FILE]...

Merkelize a file

positional arguments:
  file                  file to merkelize

optional arguments:
  -dc DEEP_COMPARE, --deep-compare DEEP_COMPARE
                        compare two files
  -c COMPARE, --compare COMPARE
                        compare files
  -p, --pretty-print    verbose output
```

## Examples
Generate Merkle Tree for a File
```
$ ./merkleizer path/to/file
Root hash: <root_hash>
```

Compare
```
$ ./merkleizer path/to/file1 -c path/to/file2
Comparing files
Files are <different>/<the same>
```
Builds merkle trees from the two files and compares their root hashes.

Deep Compare two files using Merkle Trees
```
$ ./merkleizer path/to/file1 -dc path/to/file2
Comparing files
Differences: [<indexes of differing chunks>]
```
Recurses on nodes that have different hashes in the two trees looking for different leaves.

Pretty Print (needs improvement)
```
$ ./merkleizer path/to/your/file -p
Pretty print:
8413b 8413b ef335 c77f5 4d62a e87b8 af4b5 29747 4f437 8413b
2ba30 47a75 6651c a0aca aad3c
d7578 75894 9be3b
9dd69 44e29
610dd
```

For aesthetic purposes I kept only the first 5 bytes of every hash, the script actually displays the whole hash.
