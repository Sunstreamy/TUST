package lab01; // 如果 lab01 是一个包，需要这个声明

import java.util.Arrays; // 用于数组排序

public class Task2 { // 类名与文件名 Task2.java 匹配

    public static void main(String[] args) {
        System.out.println("--- 任务二：对字符串中的所有字符排序 ---");

        String originalString = "programmingisfun"; // 示例字符串
        System.out.println("原始字符串: " + originalString);

        // 1. 将字符串转换为字符数组，因为字符串是不可变的，不能直接排序
        char[] charArray = originalString.toCharArray();

        // 2. 使用 Arrays.sort() 方法对字符数组进行排序
        Arrays.sort(charArray);

        // 3. 将排序后的字符数组转换回字符串
        String sortedString = new String(charArray);

        // 4. 输出排序后的字符串
        System.out.println("排序后的字符串: " + sortedString);

        // 可以再测试一个不同的字符串
        String anotherString = "HelloJava";
        System.out.println("\n另一个原始字符串: " + anotherString);
        charArray = anotherString.toCharArray();
        Arrays.sort(charArray);
        sortedString = new String(charArray);
        System.out.println("另一个排序后的字符串: " + sortedString);
    }
}
