'''
Step 1. Move N-1 disks from the start pole to the intermediate pole
Step 2. Move Nth disk from the start pole to the final pole
Step 3. Move N-1 disks from the intermediate pole to the final pole
'''

# First Trying with 2 disks of size - 1,2
'''
Poles s m e, objective move from s to e
input 1,2 :s
Expected output :
1. 1-sm
2. 2-se
3. 1-me

'''
print("Move 1 from start to middle")
print("Move 2 from start to end")
print("Move 1 from middle to end")


# First Trying with 3 disks of size - 1,2,3
'''
Poles s m e, objective move from s to e
input 1,2 :s
Expected output :
1. 1-sm
2. 2-se
3. 1-me

'''

def hanoi(disk, start='START', end='END', middle='MIDDLE'):
    if disk > 0:
        hanoi(disk - 1, start, middle, end)
        print('hanoi :: Move disk' + str(disk) + ' from ' + start + ' to ' + end) # Move the N disk
        hanoi(disk - 1, middle, end, start)

def myhanoi(disk, frm, to):
    start = 'START'
    end = 'END'
    middle = 'MIDDLE'
    if disk > 0:
        myhanoi(disk - 1, start, middle)
        print('myhanoi :: Move disk' + str(disk) + ' from ' + frm + ' to ' + to) # Move the N disk
        myhanoi(disk - 1, middle, end)

        
size = int(input('How many disks you wanna play? '))
myhanoi(size, 'START', 'END')

hanoi(size)
