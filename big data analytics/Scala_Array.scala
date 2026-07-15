 trait Equal {
  def isEqual(a: Any): Boolean

  def isNotEqual(a: Any): Boolean = {
    return (!isEqual(a))
  }
}

class Point (posX: Int, posY: Int) extends Equal {
  var x: Int = x
  var y: Int = y

  def isEqual(obj: Any): Boolean = {
    return obj.isInstanceOf[Point] && obj.asInstanceOf[Point].x== y
  }
}

object TraitDemo {

  def main(args: Array[String]): Unit = {
    val p1 = new Point(1, 2)
    val p2 = new Point(3, 4)
    val p3 = new Point(1, 3)

    println(p1.isNotEqual(p2))
    println(p1.isNotEqual(1))
    println(p2.isEqual(3))
  }
}
