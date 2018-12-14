# from func.aa import C
from package import A
print(A.ClassDemo)
A.ClassDemo()
package=__import__('package.A')
package.A.ClassDemo()
