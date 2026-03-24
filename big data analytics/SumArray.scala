object SumArray { 
    def main(args: Array[String]): Unit = {
        var nums = Array(1.2, 1.7, 1.12, 1.16, 1.81, 1.99)
        println("Original Array elements:")
        // Print all the array elements
        for ( x <- nums ) {
            print(s"${x}, ") 
        }
        println("\nUsing sum():")
        val result = nums.sum
        println(s"Result: ${result}"); 
        println("\nUsing for loop:")
        var total = 0.0; 
        for (i <- 0 to (nums.length - 1)) {
            total += nums(i);
        }
        println(s"Result: ${total}");
    }
}