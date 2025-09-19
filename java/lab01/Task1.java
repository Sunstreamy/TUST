package lab01; // 如果 lab01 是一个包，需要这个声明

import java.util.Random; // 用于生成随机数

public class Task1 { // 类名与文件名 Task1.java 匹配

    public static void main(String[] args) {
        System.out.println("--- 任务一：创建并显示 5x5 整数矩阵 ---");

        // 1. 创建一个 5x5 的整数矩阵 (二维数组)
        int[][] matrix = new int[5][5];

        // 用于生成随机数的对象
        Random random = new Random();

        // 2. 填充矩阵 (这里用 0 到 99 之间的随机数填充)
        for (int i = 0; i < 5; i++) { // 遍历行
            for (int j = 0; j < 5; j++) { // 遍历列
                matrix[i][j] = random.nextInt(100); // 生成 0 到 99 之间的随机整数
            }
        }

        // 3. 输出显示矩阵
        System.out.println("生成的 5x5 矩阵如下：");
        for (int i = 0; i < 5; i++) { // 遍历行
            for (int j = 0; j < 5; j++) { // 遍历列
                // 为了对齐，使用 printf 格式化输出，%4d 表示至少占4个字符宽度
                System.out.printf("%4d", matrix[i][j]);
            }
            System.out.println(); // 每行结束后换行
        }
    }
}
