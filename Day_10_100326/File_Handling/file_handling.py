'''
File Handling:
-- file is a type of container in which we contain or store some data.
-- by using extension name, we can identify what type of data is there inside of it.
example: .py, .mp4, .html, .mp3, .png, .jpg, .jpeg, etc
-- before handling any file, taking permission is very much important.
   open():
   open('filename.extension'/'absolute path', mode)

-- here, total 3 different modes are present:
1. write(w)
2. read(r)
3. append(a)

# write mode:
1. only write(w),
2. write + read (w+)
3. write binary (wb)
4. write & read binary (wb+)

# read mode:
1. only read(r),
2. read + write (r+)
3. read binary (rb)
4. read & write binary (rb+)

# append mode:
1. only append(a),
2. append + read (a+)
3. append binary (ab)
4. append & read binary (ab+)

# for write operation:
1. write(str_data): single line of data
2. writelines([line1, line2, ....., linen ]): multiple line of data

# NOTE:
1. in this, if the file isnt present, it will create one then perform write operation.
2. if the file is already present, then it will override prev data with the new one. 



'''
