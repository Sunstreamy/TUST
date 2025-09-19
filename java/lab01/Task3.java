package lab01; // 如果 lab01 是一个包，需要这个声明

import java.util.InputMismatchException; // 用于处理输入类型不匹配的异常
import java.util.Scanner; // 用于从键盘读取用户输入

public class Task3 { // 类名与文件名 Task3.java 匹配

    public static void main(String[] args) {
        System.out.println("--- 任务三：读取 double 数并输出整数和小数部分 ---");

        // 创建 Scanner 对象用于读取用户输入
        Scanner scanner = new Scanner(System.in);
        double number = 0;

        try {
            System.out.print("请输入一个 double 型数: ");
            number = scanner.nextDouble(); // 读取 double 类型输入
        } catch (InputMismatchException e) {
            System.out.println("输入无效！请输入一个有效的数字。");
            return; // 结束方法，不再继续执行
        } finally {
            // 无论是否发生异常，都要关闭 Scanner 对象以释放系统资源
            // 非常重要！在程序不再需要读取输入时应关闭
            scanner.close();
        }

        // 1. 获取整数部分
        // 将 double 类型强制转换为 int 类型，会自动截断小数部分
        int integerPart = (int) number;

        // 2. 获取小数部分
        // 小数部分 = 原始 double 数 - 整数部分
        // 注意：由于浮点数精度问题，小数部分可能不会是精确的0.x，但对于此任务通常足够
        // 使用 Math.abs() 确保小数部分显示为正值，更符合直观理解
        double fractionalPart = Math.abs(number - integerPart);

        // 3. 输出结果
        System.out.println("您输入的数是: " + number);
        System.out.println("整数部分是: " + integerPart);
        // 为了美观，对小数部分进行格式化，保留四位小数
        System.out.printf("小数部分是: %.4f%n", fractionalPart);
    }
}
