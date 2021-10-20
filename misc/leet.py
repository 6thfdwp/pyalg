from collections import defaultdict


def findDuplicate(paths):
    """
    :type paths: List[str]
    :rtype: List[List[str]]
    each item in the input is files under same dir
    <dir1 file() file2()>, <dir2 file3()>
    
    file name and content only letteres and digits, and length is 
    consider inverted index with content as key, list of file path containing that content
    """
    findex = defaultdict(list)
    
    for i, files in enumerate(paths):
      flist = files.split(' ')
      d = flist[0] # dirname

      for fi in xrange(1, len(flist)):
        f = flist[fi]
        # l = f.find('(')
        fname, _, content = f.partition('(')
        # print fname, content[:-1]

        fpath = d + '/' + fname
        findex[content[:-1]].append(fpath)
        
    return [ flist for flist in findex.values() ]
            
if __name__ == '__main__':
    P = [ 87, 14, 25, 41, 17, 48, 42, 15, 74, 45, 73, 20, 11, 39, 54, 5, 29, 53, 89, 66, 56, 4, 60, 98, 92, 20, 16, 80 ]
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    print findDuplicate(paths)
