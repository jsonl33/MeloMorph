var dropZone = document.getElementById('drop-zone');
var fileInput = document.getElementById('file-input');

// 드래그 앤 드롭 영역에 마우스 오버 시 스타일 변경
dropZone.addEventListener('dragover', function(e) {
  e.preventDefault();
  dropZone.style.backgroundColor = '#f0f0f0';
});

// 드래그 앤 드롭 영역에서 마우스 벗어날 시 스타일 복원
dropZone.addEventListener('dragleave', function(e) {
  e.preventDefault();
  dropZone.style.backgroundColor = '';
});

// 파일 드롭 시 처리
dropZone.addEventListener('drop', function(e) {
  e.preventDefault();
  dropZone.style.backgroundColor = '';
  var files = e.dataTransfer.files;
  fileInput.files = files;
});

// 클릭 시 파일 선택 창 열기
dropZone.addEventListener('click', function() {
  fileInput.click();
});

// 폼 제출 로직
document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var formData = new FormData(this);
    fetch('/upload/', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        document.getElementById('result').innerText = '음악 파일의 길이: ' + data.duration + ' 밀리초';
      } else {
        document.getElementById('result').innerText = '업로드 실패';
      }
    });
  });