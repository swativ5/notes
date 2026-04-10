object Demo {
    def math(x: Double, y: Double, f: (Double, Double) => Double): Double = {
        f(x, y)
    }
    def createMultiplier(n: Int) : Int => Int = {
        (x: Int) => x * n
    }
    def main(args: Array[String]): Unit = {
        // val result = math(50, 20, (x, y) => x + y)
        // val result1 = math(50, 20, (x, y) => x * y)
        // val result2 = math(50, 20, (x, y) => x min y)
        // val result3 = math(50, 20, (x, y) => x max y)
        // println(result)
        // println(result1)
        // println(result2)
        // println(result3)
        val multiplierby2 = createMultiplier(2)
        val multiplierby3 = createMultiplier(3)

        val result1 = multiplierby2(4)
        val result2 = multiplierby3(4)
        print(result1)
        print(result2)
    }
}