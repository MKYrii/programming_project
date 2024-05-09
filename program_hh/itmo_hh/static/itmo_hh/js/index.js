let res_flag = 0;

resume_frame.onclick = async function() {
	if (res_flag == 0){
	    for(let i = 0; i < 50; i++){
	    	await new Promise(resolve => setTimeout(resolve, 5));
	        resume_frame1.style.left = 980 - i * 6 + 'px';
	        resume_frame2.style.top = 675 - i * 2  + 'px';
	        resume_frame.style.background = '#d9d9d9';
	        horizont_line.style.left = 980 - i * 6 + 'px';
	        horizont_line.style.width = 1 + i * 6 + 'px';
	        vertical_line.style.left = 1097 - i + 'px';
	        vertical_line.style.width = 1 + i * 2 + 'px';
	    }
	    res_flag = 1;

	}
}

bod.onclick = async function() {
	if (res_flag == 1){
		for(let i = 0; i < 51; i++){
	    	await new Promise(resolve => setTimeout(resolve, 5));
	        resume_frame1.style.left = 680 + i * 6 + 'px';
	        resume_frame2.style.top = 575 + i * 2  + 'px';
	        resume_frame.style.background = 'white';
	        horizont_line.style.left = 680 + i * 6 + 'px';
	        horizont_line.style.width = 301 - i * 6 + 'px';
	        vertical_line.style.left = 1047 + i + 'px';
	        vertical_line.style.width = 101 - i * 2 + 'px';
	    }
	    res_flag = 0;
	    
    }
}
