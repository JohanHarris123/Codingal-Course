file_read = open(r"C:\Users\Johan\Desktop\Codingal Course\M9\Classwork Activity\Codingal.txt", 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open(r"C:\Users\Johan\Desktop\Codingal Course\M9\Classwork Activity\Codingal.txt", 'w')
file_write.write("File in write mode...\n")
file_write.write("Hi! I am a Penguin. I am 1 yr. old\n")
file_write.close()

file_append = open(r"C:\Users\Johan\Desktop\Codingal Course\M9\Classwork Activity\Codingal.txt", 'a')
file_append.write("\nFile in append mode...")
file_append.write("Hi! I am a Penguin. I am 1 yr. old")
file_append.close()