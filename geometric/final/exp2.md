
## 样例 2

### 问题描述
河边点 O 的正对岸为点 A, 河宽 OA=10m, 水流速度为 1m/s, 有一只鸭子从点 A 游向点 O。设鸭子游速为 2m/s, 且鸭子游动的方向始终朝着点 O, 确定鸭子游动的轨迹及任一时刻鸭子的具体位置。

### 求解过程
**模型假设：** 河宽固定，两岸平行

**模型建立：** 取 O 为坐标原点，河岸顺水方向为 x 轴，y 轴指向对岸。

设鸭子 t 时刻在水中位置坐标为 (x, y), **目标：** 确定坐标 (x, y) 关于时间 t 的函数并绘图。

(图片：鸭子游动示意图，左侧)
(图片：鸭子游动示意图，右侧)

设鸭子速度方向与 x 轴正向夹角为 θ，由运动方程得
```math
\begin{cases}
\frac{dx}{dt} = b\cos(\pi - \theta) + a \\
\frac{dy}{dt} = -b\sin(\pi - \theta)
\end{cases}
\quad \text{即} \quad
\begin{cases}
\frac{dx}{dt} = a - \frac{bx}{\sqrt{x^2 + y^2}} \\
\frac{dy}{dt} = \frac{-by}{\sqrt{x^2 + y^2}}
\end{cases}
```
**初始条件：** x(0) = 0, y(0) = 10

---

**Matlab 程序如下：**

**(1) 创建 M 文件**
```matlab
function dx=duhe(t,x)

a=1; b=2;

s=sqrt(x(1)^2+x(2)^2);

dx=[a-b*x(1)/s; -b*x(2)/s]; % Note: Image shows dx=[a-b*x(1)/s;-b*x(2)/s] but only one line for dx. Assuming it's a vector.
% Corrected the second component based on the derived dy/dt formula.
% The image's dx=[a-b*x(1)/s;-b*x(2)/s] is a single line, implying dx is a row vector.
% For ode45, dx should be a column vector.
% The formula dy/dt = -by/sqrt(x^2+y^2) corresponds to dx(2) = -b*x(2)/s.
end
```
*Self-correction from image: The image shows `dx=[a-b*x(1)/s;-b*x(2)/s]` as a single line. MATLAB interprets semicolon inside brackets as a row separator for matrices or a command separator. For function output for ODE solvers, `dx` should be a column vector representing `[dx/dt; dy/dt]`. The image line `dx=[a-b*x(1)/s;-b*x(2)/s]` is correct syntax for creating a column vector in MATLAB.*

**(2) 创建主程序**
```matlab
clc
clear
t=0:0.5:7;

x0=[0,10]; %x、y 的初始值
[t,x]=ode45(@duhe,t,x0); %调用 ode45 计算, @duhe 为函数句柄或文件名

% [t,x]%输出 t,x(t),y(t) % This line is a comment in the image
plot(x(:,1),x(:,2)) %按照数值输出作 x(t), y(t) 的图形
```