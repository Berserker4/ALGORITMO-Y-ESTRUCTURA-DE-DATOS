from package.ClassQueue import Queue

cola_1 = Queue()

cola_1.arrive(1)
cola_1.arrive(2)
cola_1.arrive(3)
cola_1.arrive(4)
cola_1.arrive(5)
cola_1.attention()
cola_1.attention()
print(cola_1.size())
print(cola_1.on_front())
cola_1.move_to_end()
cola_1.move_to_end() 
print()
for i in range(cola_1.size()):
     print(cola_1.on_front())
     cola_1.move_to_end()
print()
print(cola_1.size())