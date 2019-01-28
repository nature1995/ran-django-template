
$(function(){
	preGame();
	newGame();
	$(document).keydown(function(event){
		if(event.keyCode==38||event.keyCode==40||event.keyCode==37||event.keyCode==39){
			if(!overFlag){
				moveCells(event.keyCode);				
			}
			return false;
		}
	});
	document.addEventListener('touchstart',function(event){
		startX = event.touches[0].pageX;
		startY = event.touches[0].pageY;		
	});
	document.addEventListener('touchmove',function(event){
		event.preventDefault();
	});
	document.addEventListener('touchend',function(event){
		endX = event.changedTouches[0].pageX;
		endY = event.changedTouches[0].pageY;

		if(Math.abs(endX-startX)>dw*0.2||Math.abs(endY-startY)>dw*0.2){
			if(Math.abs(endX-startX)>Math.abs(endY-startY)){
				//左右
				if(endX-startX>0){
					//38上//40下//37左//39右
					//右
					moveCells(39);		
				}else{
					//左
					moveCells(37);
				}
			}else{
				if(endY-startY>0){
					//下
					moveCells(40);
				}else{
					//上
					moveCells(38);
				}
			}
		}
	});
});

function moveCells(key){
	changeCells(key);
	randomOneNumber();
	setTimeout(function(){
		updateNumberCells();					
	},100);	
	$('#score').text(score);
	if(nospace()&&cannotMove()){
		overFlag = true;
		setTimeout('showOver()',100);
	}
}

function preGame(){
	if(dw>=500){
		paneWidth = 500;
		cellPadding = 20;
		cellWidth = 100;
	}	
	gamePane.css({'width':paneWidth-2*cellPadding,'height':paneWidth-2*cellPadding,'padding':cellPadding});
	for(var i=0;i<4;i++){
		for(var j=0;j<4;j++){
			gamePane.append('<div class="cell" id="cell-'+i+'-'+j+'"></div>');
			$('#cell-'+i+'-'+j)
							  .css('width',cellWidth)
							  .css('height',cellWidth)
							  .css('left',getLeft(j))
							  .css('top',getTop(i));
		}
	}
}

function newGame(){
	init();	
	updateNumberCells();
	randomOneNumber();
	randomOneNumber();	
}

function init(){
	for(var i=0;i<4;i++){
		cells[i]=new Array(4);
	}
	score = 0;
	$('#score').text(score);
	overFlag=false;
	$('#game-pane .over').remove();
}

function updateNumberCells(){
	$('.number-cell').remove();
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(cells[i][j]){
				var number = cells[i][j];
				gamePane.append('<div class="number-cell" id="number-cell-'+i+'-'+j+'"></div>');
				$('#number-cell-'+i+'-'+j)
						 .css('width',cellWidth)
						 .css('height',cellWidth)
						 .css('left',getLeft(j))
						 .css('top',getTop(i))
						 .css('line-height',cellWidth+'px')
						 .css('background-color',getBgColor(number))
						 .css('color',getNumberColor(number))
						 .text(number);
				if(number>=16){
					$('#number-cell-'+i+'-'+j).css('font-size','50px');
				}
				if(number>=128){
					$('#number-cell-'+i+'-'+j).css('font-size','40px');
				}
				if(number>=1024){
					$('#number-cell-'+i+'-'+j).css('font-size','30px');
				}
				if(number>=16384){
					$('#number-cell-'+i+'-'+j).css('font-size','20px');
				}
			}
		}
	}
}