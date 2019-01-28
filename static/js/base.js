var cells = new Array(4);
var score = 0;
var overFlag = false;
var dw = window.screen.availWidth;
var paneWidth = dw*0.92;
var cellWidth = dw*0.18;
var cellPadding = dw*0.04;
var startX;
var startY;
var endX;
var endY;
var addflag = new Array(4);
var gamePane = $('#game-pane');

function getLeft(j){
	return (cellWidth+cellPadding)*j+cellPadding+'px';
}

function getTop(i){
	return (cellWidth+cellPadding)*i+cellPadding+'px';
}

function getBgColor(number){
	switch(number){
		case 2:return '#eee4da';
		case 4:return '#ede0c8';
		case 8:return '#f2b179';
		case 16:return '#f59563';
		case 32:return '#f67e5f';
		case 64:return '#f65e3b';
		case 128:return '#edcc61';
		case 512:return '#9c0';
		default:return '#33b5e5';
	}
}

function getNumberColor(number){
	if(number<=4){
		return '#776e65';
	}
	return '#000';
}

function randomOneNumber(){
	if(nospace()){
		return false;
	}
	var count = 20;	
	do{
		//生成两个0-3的随机数
		var i = Math.floor(Math.random()*count%4);
		var j = Math.floor(Math.random()*4);
		//判断这个位置是否可用
		if(!hasNumber(i,j)){
			cells[i][j]= Math.random()<0.5 ? 2:4;
			popShowCell(i,j,cells[i][j]);
			return true;
		}
		count--;
	}while(count!=0);
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(!cells[i][j]){
				cells[i][j]=Math.random()<0.5 ? 2:4;
				popShowCell(i,j,cells[i][j]);				
				return true;
			}
	return false;
}

function nospace(){
	for(var i=0;i<4;i++){
		for(var j=0;j<4;j++){
			if(!cells[i][j]){
				return false;
			}
		}
	}
	return true;
}

function countNull(){
	var count=0;
	for(var i=0;i<4;i++){
		for(var j=0;j<4;j++){
			if(!cells[i][j]){
				count++;				
			}
		}
	}
	return count;
}

function hasNumber(i,j){
	if(cells[i][j]){
		return true;
	}

	return false;
}

function popShowCell(i,j,number){
	gamePane.append('<div class="number-cell" id="number-cell-'+i+'-'+j+'"></div>');
	$('#number-cell-'+i+'-'+j)
						 .css('width',cellWidth+'px')
						 .css('height',cellWidth+'px')
						 .css('left',getLeft(j))
						 .css('top',getTop(i))
						 .css('line-height',cellWidth+'px')
						 .css('background-color',getBgColor(number))
					     .css('color',getNumberColor(number))
					     .css('display','none')
					     .text(number);
	$('#number-cell-'+i+'-'+j).show(90);
}

function changeCells(key){
	for(var i=0;i<4;i++)
		addflag[i] = new Array(4);
	//38上//40下//37左//39右
	switch(key){
		case 38:upAction(); break;
		case 40:downAction(); break;
		case 37:leftAction(); break;
		case 39:rightAction(); break;
		default:return;
	}
}

function upAction(){
	for(var i=1;i<4;i++){
		for(var j=0;j<4;j++){
			if(cells[i][j]){				
				moveCell(i,j,cells[i][j],-1,1,0);	
			}
		}
	}
}

function downAction(){
	for(var i=2;i>=0;i--){
		for(var j=0;j<4;j++){
			if(cells[i][j]){				
				moveCell(i,j,cells[i][j],+1,1,3);	
			}
		}
	}
}

function leftAction(){
	for(var j=1;j<4;j++){
		for(var i=0;i<4;i++){
			if(cells[i][j]){				
				moveCell(i,j,cells[i][j],-1,2,0);
			}
		}
	}
}

function rightAction(){
	for(var j=2;j>=0;j--){
		for(var i=0;i<4;i++){
			if(cells[i][j]){				
				moveCell(i,j,cells[i][j],+1,2,3);
			}
		}
	}
}

/**
type = 1;上下type = 2;左右
*/
function moveCell(i,j,temp,offset,type,end){
	var startI = i;
	var startJ = j;
	var endI = i;
	var endJ = j;	
	if(type==1){
		while(i!=end){
			i+=offset;
			n = cells[i][j];
			if(n){
				if( n==temp && !addflag[i][j]){
					temp += n;
					addflag[i][j]=true;					
					cells[i-offset][j]=null;
					cells[i][j]=temp;
					score+=temp;
					endI = i;
					endJ = j;
					break;	
				}else{
					endI = i-offset;
					endJ = j;			
					break;
				}
			}else{
				cells[i-offset][j]=null;
				cells[i][j]=temp;
				if(i==end){
					endI = i-offset;
					endJ = j;
					break;
				}
			}
		}	
	}else if (type==2) {
		while(j!=end){
			j+=offset;
			n = cells[i][j];
			if(n){
				if( n==temp && !addflag[i][j]){
					temp += n;
					addflag[i][j]=true;	
					cells[i][j-offset]=null;			
					cells[i][j]=temp;	
					score+=temp;	
					endI = i;
					endJ = j;			
					break;	
				}else{	
					endI = i;
					endJ = j-offset;		
					break;
				}
			}else{
				cells[i][j-offset]=null;
				cells[i][j]=temp;
				if(j==end){
					endI = i;
					endJ = j-offset;
					break;
				}
			}
		}	
	}
	//移动的动画
	if(!(startI==endI&&startJ==endJ)){
		$('#number-cell-'+startI+'-'+startJ).animate({
			left:getLeft(endJ),
			top:getTop(endI)
		},100);	
	}
}

function cannotMove(){
	for(var i=0;i<4;i++){
		for(var j=0;j<4;j++){
			if(cells[i][j]){
				if(canMove(i,j)){
					return false;
				}
			}
		}
	}		
	return true;
}

function showOver(){
	gamePane.append('<div class="over"><p>游戏结束</p><a href="javascript:newGame();">重新开始</a><p>你的分数是:'+score+'</p></div>');
	$('#game-pane .over').css('opacity','0.7')
						 .css('width',paneWidth/2)
						 .css('height',paneWidth/2)
						 .css('padding',paneWidth/4);						 
	setTimeout(function(){
		$('#game-pane .over').fadeIn(800);
	},300);
}

function canMove(i,j){
	//上下左右判断是否有同值
	if(i!=3&&cells[i+1][j]==cells[i][j]){
		return true;
	}
	if(i!=0&&cells[i-1][j]==cells[i][j]){
		return true;
	}
	if(j!=3&&cells[i][j+1]==cells[i][j]){
		return true;
	}
	if(j!=0&&cells[i][j-1]==cells[i][j]){
		return true;
	}
	return false;
}