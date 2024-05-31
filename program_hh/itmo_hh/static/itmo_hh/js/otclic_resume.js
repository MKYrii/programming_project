


search_btn = document.getElementsByName("search_btn");

search_btn.style.width = 100 / resumes_length + '%';

otklik_btn.onclick = async function() {
        for(let i = 0; i < 50; i++){
            await new Promise(resolve => setTimeout(resolve, 5));
            data_frame.style.width = 200 + i * 5;
            data_frame.style.height = 40 + i * 5;
        }
        
        }
        s_btn.style.left = 1000;
        data_frame.style.height = 1000;

     
        search_btn.style.width = 100 / resumes_length + '%';
    
    alert('hello');
