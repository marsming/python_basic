class A:

	def run(self):
		print("running")


class B:

	def sleep(self):
		print("sleeping")


class C(A,B):
	pass


c = C()
c.run()
c.sleep()