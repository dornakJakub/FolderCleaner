# folderCleaner

Script for deleting files based on matching RegEx pattern.
Default values are set to clean downloads folder from recordings of cypress tests.

<b>usage: python main\.py \<folder_path> \<pattern></b>

### Return codes:
0   All good
5   Directory doesn't exist
6   Permission denied
7   Other OS related error