
import sys # 파이썬에 기본적으로 내장되어 있는 sys 모듈을 불러온다. 이 모듈은 명령 줄에서
             # 추가적으로 입력된 인수를 스크립트로 넘겨준다.

# input_file = sys.argv[1] # sys 모듈의 argv라는 인수를 사용하는데, 이 인수는 명령줄 실행 시
# output_file = sys.argv[2] # 추가적으로 입력되는 인수를 리스트 자료형으로 받는다.
input_file = "C:\Python\Python36-32\supplier_data.csv"
output_file = "C:\Python\Python36-32\out_data.csv"


with open(input_file, 'r', newline='') as filereader: # 파일 객체를 열어주며,
 # open() 함수에서 ‘r'은 읽기 모드를 할당한다. 이는 input_file이 읽기 위해 열렸음을 의미한다.
   with open(output_file, 'w', newline='') as filewriter: # 파일 객체를 열어주며,
      # ‘w'는 쓰기 모드를 할당하고 output_file은 쓰기 위해 열렸음을 의미한다.
      # 또한, with 문은 with 문이 종료될 때 자동으로 파일 객체를 닫는다.
      header = filereader.readline() # readline() 함수를 사용하여 입력 파일의 첫 번째
             # 행(헤더 행)을 문자열로 읽고 이를 header라는 변수에 할당한다.
      header = header.strip() # strip() 함수를 사용하여 header에 있는 문자열의 양끝에서
                        # 공백, 탭 및 개행문자(\n) 등을 제거한 뒤 header에 다시 할당한다.
      header_list = header.split(',') # split() 함수를 사용하여 문자열을 쉼표 기준
                 # 으로 구분하여 리스트에 할당하며, 리스트의 각 원소는 입력 파일의 각 열의
                 # 헤더이며, header_LIST라는 변수로 할당된다.
      print(header_list) # HEADER_LIST의 값(즉, 헤더 행)을 화면에 출력한다.
      filewriter.write(','.join(map(str,header_list))+'\n') # write() 함수를
           # 사용하여 header_list의 각 값을 출력 파일에 쓴다. map() 함수는 header_list의 각
           # 원소에 str() 함수를 적용하여 각원소를 문자열로 만들고 join() 함수는 header_list의
           # 각 값 사이에 쉼표를 삽입하고 리스트 문자열로 변환한다. 그 다음 개행 문자를 문자열
           # 끝에 추가하며, filewriter 객체는 그 문자열을 출력 파일의 첫 번째 행에 기록한다.
      for row in filereader: # for 문을 사용하여 입력 파일의 나머지 행을 반복한다.
          row = row.strip()
          row_list = row.split(',')
          print(row_list)
          filewriter.write(','.join(map(str,row_list))+'\n')
