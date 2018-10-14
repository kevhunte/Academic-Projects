#	Lab 3 #	Recursive Fibonacci function

	.data				#data segment
name:	.asciiz "CSE3666: Lab 3: Kevin Hunte(kmh14012)\nEnter an integer:"
msg0:	.asciiz "F(%d) cannot be computed.\n"
msg1:	.asciiz "F(%d) = (%d)\n"		

	.align 2
buffer: .space 8		# reserve space for two words 
n_in:	.space 4		# get input from the user

	.text			# Code segment
	.globl	main		# declare main to be global

main:		
	la	$a0, name
	jal	printf		# call printf function

	li	$s0, 49
	li	$v0, 5		#read an integer
	syscall
	move	$s0, $v0	#save the user input
	
	la	$s1, buffer	# buffer

	#call jal
	move	$a0, $s0	# set the 1st argument. user input, n
	move	$a1, $s1	# set the 2nd argument. array p
	jal 	Fibonacci2
	bne	$v0, $zero, l_ok

	# 0 is returned
	la	$a0,msg0	# $a0 := address of message 1
	move	$a1, $s0	# the number
	jal	printf
	j	Exit
	
l_ok:
	la	$a0, msg1
	move	$a1, $s0	
	lw	$a2, ($s1)	# p[0] is F(n) 
	jal	printf

Exit:	li	$v0,10		# System call, type 10, standard exit
	syscall			# ...and call the OS

# Fibonacci2(n, p)
#	Used registers
#	t0, truth val of n<=0

Fibonacci2:
	addi	$sp, $sp, -12
	sw	$ra, 0($sp)	#starting address
	sw	$a0, 4($sp)	#n
	sw	$s2, 8($sp)	#return val
	
	li	$t3, 1
	slt 	$t0, $a0, $t3 	#n<1 equivalent to n<=0
	beq	$t0, 1, ret0	#if n<=0, return 0
	bne	$a0, 1, comp	#if n!=1, skip to fib(n-1,p)
	li	$t0, 0		#reused register
	sll	$t1, $t0, 2	#offset of 0
	add	$t2, $a1, $t1	#address of p[0]
	sw	$t3, ($t2)	#p[0]=1
	sll	$t4, $t3, 2	#offset of 1
	add	$t5, $a1, $t4	#address of p[1]
	sw	$t0, ($t5)	#p[1]=0
	j 	ret1		#goto exit and return 1
comp:
	add	$a0, $a0, -1	#n-=1
	j	Fibonacci2	
	move	$s2, $v0	#r= return val for function
	beq	$s2, 0, ret0	#r==0, return 0
	lw	$t6, ($t2)	#val in p[0]
	lw	$t7, ($t5)	#val in p[1]
	add	$s2, $t6, $t7	#r=p[0]+p[1]
	sltu	$t0, $s2, $t6	#if r<p[0], sum not calc correctly
	bne	$t0, 0, ret0	#if overflow, return 0
	sw	$t6, ($t5)	#p[1]=p[0]
	sw	$s2, ($t2)	#p[0]=r
	j 	ret1		#return 1	

ret0:	
	li	$v0, 0		# return error for now.
	j	end		#skip other return val
ret1:	
	li	$v0, 1		# returns 1
end:	
	lw	$ra, 0($sp)	#starting address
	lw	$a0, 4($sp)	#n
	lw	$s2, 8($sp)	#return val
	addi	$sp, $sp, 12	#restore pointer
	jr	$ra
