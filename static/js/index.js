$(function ()
{
	console.log('start jquery, Hey')
	var IRCodeList=$('#IRCodeList')
	var remoteController=$('#remote-controller'),
//	$.ajax({
//		url:'https://morita.website/ir/codes'
//	})
//		.done(function(codes){
//			for(let k in codes){
//				if(codes.hasOwnProperty(k)){
//					makeIRCodeli(k,codes[k])
//				}
//			}
//		})			
	remoconList=[
		["電源"],
		["開/閉","TV入力切換","音声切換","オフタイマー"],
		["TV","チューナー","BD"],
		["","DVD","AMP"],
		["アナログ","デジタル","BS","CS"],
		["1","2","3"],
		["4","5","6"],
		["7","8","9"],
		["10","11","12"]
	]
	for(var i=0,len=remoconList.length;i<len;len++){
		var column=12/len,
			row=remoconList[i],
			$row=$('<div class="row"></div>')
		//for(var j=0,rowLen=row.length;j<rowLen;rowLen++){
		//	var col=row[j],
		//	$col=$(`<div class="col-xs-${column}"></div>`)
		//	if(col){
		//		$col.append($(`<button>${col}</button>`,{
		//			on:{
		//				click:function (e) {
		//					e.preventDefault()
////							$.ajax(
////								{
////									type:'POST',
////									url:'https://morita.website/ir/code'
////									data:{
////										phrase:col
////									}
////								}
////							)
////							.done(function (d) {
////								console.log(d);
////							})
		//				}
		//			}
		//		}))
		//	}
		//  $row.append($col)
		//}
		remoteController.append($row)
	}
//	$('#addIRCode')
//		.on('submit', function (e)
//		{
//			e.preventDefault()
//			console.log($('#name')
//				.val())
//			console.log('clicked ircode')
//			$.ajax(
//				{
//					url: 'https://morita.website/ir/code-from/' + $('#memo_no')
//						.val(),
//				})
//				.done(function (code)
//				{
//					console.log(code);
//					$.ajax(
//						{
//							url: 'https://morita.website/ir/addcode',
//							type: 'POST',
//							data:
//							{
//								name: $('#name')
//									.val(),
//								code: code
//							}
//						})
//						.done(function (d)
//						{
//							makeIRCodeli(d.name,d.code)
//							console.log(d)
//						})
//				})
//		})
	//function IRCodeButton(name,code){
	//	var button = $('<button type="button" class="btn btn-primary">' + name+ '</button>')
//
	//	$(IRli)
	//		.click(
	//			function (event)
	//			{
	//				event.preventDefault()
	//				$.ajax(
	//					{
	//						url: 'https://morita.website/ir/code',
	//						type: 'POST',
	//						data:
	//						{
	//							'code': code
	//						}
	//					})
	//					.done(function (data)
	//					{
	//						console.log(data)
	//					})
	//			})
	//	return button
	//}
});
