'''
① 3+6+9+12+...+N形态，
加上3的倍数。
 ② 输入一个数字。
 ③ 使用while重复句编写程序，以确定3的倍数总和超过输入数字时的N值和总和，
 N值是第几位。
'''
var num, sum=0, count; 
num=parseInt(prompt("숫자 입력"));
document.write("사용자 입력 : "+num+"<br>");
for(count=3; count<=num; count+=3)
{ 
 sum+=count; 
} 
document.write(num+"을(를) 넘었을 때의 값 : "+count+"<br>");
document.write(num+"을(를) 넘었을 때까지의 총 합계 : "+sum+"<br>");
document.write(num+"을(를) 넘었을 때까지 몇 번째 3의 배수인가 : "+count/3);
