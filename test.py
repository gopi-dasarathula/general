class A:
	pass
class B(A):
	pass
class C(B):
	pass
for i in [C,B,A]:
	try:
		raise i()
 	except A:
 		print "in A"
 	except B:
 		print "in B"
 	except C:
		print "in C"
	finally:
		print "in finally"
 