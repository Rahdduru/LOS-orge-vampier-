#LOS
=========
LORD OF SQL INJECTION 풀이
---------
### #orge#

orc와 풀이 방법이 똑같은 문제이다.<br>
if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); <br>
다만 이 함수를 보면 and와 or을 string 형태로 입력하면 필터링이 된다.<br><br>

이 경우 &&(AND)와 ||(OR)로 우회가 가능하다.<br>
그러나 이번 문제는 and나 or을 사용하지 않아도 python코드를 이용해 substr코드를 작성해 풀어주면 된다.<br>
(master branch로 가면 작성한 python코드가 있다.)<br><br>

python 코드를 이용해 비밀번호를 알아내면<br><br>

pw=7b751aec

### #troll#

초반 문제에 나왔던 문제 풀이 조건과 동일하다.<br>
 if($result['id'] == 'admin') solve("troll");<br>
 id가 admin이면 troll을 풀 수 있다.<br><br>
 
 그러나 if(preg_match("/admin/", $_GET[id])) exit("HeHe"); 이 쿼리문을 보면<br>
 admin을 필터링 해버린다.<br><br>
 
 이 문제의 경우 php의 함수를 조금 알아야한다.<br>
 php의 ereg함수를 이용해서 필터링을 하고 있다.<br>
 ereg함수는 대소문자를 구분하는 반면,<br>
 database는 table의 이름과 atrribute 이름에서만 대소문자 구분을 한다.<br>
 즉, database의 table 안에 있는 정보를 검색할 때 대소문자를 구분하지 않는다.<br>
 이를 이용해 이번 문제를 풀어준다.<br><br>
 
 즉, admin을 대소문자 섞어 입력해주면 troll을 풀 수 있다.<br><br>
 
 id=Admin
 
 ### #Vampire#

 if($result['id'] == 'admin') solve("vampire"); troll과 문제를 푸는 조건이 동일하다.<br>
