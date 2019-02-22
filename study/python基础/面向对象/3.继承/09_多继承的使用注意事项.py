class A:

	def run(self):
		print("A--- running")

	def sleep(self):
		print("A--- sleeping")


class B:

	def sleep(self):
		print("B--- sleeping")

	def run(self):
		print("B--- running")


class C(A,B):
	pass


c = C()
c.run()
c.sleep()