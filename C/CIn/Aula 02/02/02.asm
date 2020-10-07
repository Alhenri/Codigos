	.file	"02.c"
	.text
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "Digite x, y e z: \0"
LC1:
	.ascii "%f %f %f\0"
LC2:
	.ascii "O maior eh: %f\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB13:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$32, %esp
	call	___main
	movl	$LC0, (%esp)
	call	_printf
	leal	20(%esp), %eax
	movl	%eax, 12(%esp)
	leal	24(%esp), %eax
	movl	%eax, 8(%esp)
	leal	28(%esp), %eax
	movl	%eax, 4(%esp)
	movl	$LC1, (%esp)
	call	_scanf
	flds	20(%esp)
	flds	24(%esp)
	fcompp
	fnstsw	%ax
	sahf
	jbe	L15
	flds	24(%esp)
	jmp	L4
L15:
	flds	20(%esp)
L4:
	flds	28(%esp)
	fcompp
	fnstsw	%ax
	sahf
	jbe	L16
	flds	28(%esp)
	jmp	L7
L16:
	flds	20(%esp)
	flds	24(%esp)
	fcompp
	fnstsw	%ax
	sahf
	jbe	L17
	flds	24(%esp)
	jmp	L7
L17:
	flds	20(%esp)
L7:
	fstpl	4(%esp)
	movl	$LC2, (%esp)
	call	_printf
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE13:
	.ident	"GCC: (MinGW.org GCC Build-20200227-1) 9.2.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
	.def	_scanf;	.scl	2;	.type	32;	.endef
