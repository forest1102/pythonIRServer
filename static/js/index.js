$(function ()
{
	console.log('start jquery, Hey')
	var IRCodeList=$('#IRCodeList')
	$.ajax({
		url:'https://morita.website/ir/codes'
	})
		.done(function(codes){
			for(let k in codes){
				if(codes.hasOwnProperty(k)){
					makeIRCodeli(k,codes[k])
				}
			}
		})			
	$('#addIRCode')
		.on('submit', function (e)
		{
			e.preventDefault()
			console.log($('#name')
				.val())
			console.log('clicked ircode')
			$.ajax(
				{
					url: 'https://morita.website/ir/code-from/' + $('#memo_no')
						.val(),
				})
				.done(function (code)
				{
					console.log(code);
					$.ajax(
						{
							url: 'https://morita.website/ir/addcode',
							type: 'POST',
							data:
							{
								name: $('#name')
									.val(),
								code: code
							}
						})
						.done(function (d)
						{
							makeIRCodeli(d.name,d.code)
							console.log(d)
						})
				})
		})
	function makeIRCodeli(name,code){
		var IRli = $('<li><button type="button" class="btn btn-primary">' + name+ '</button></li>')

		$('button', IRli)
			.click(
				function (event)
				{
					event.preventDefault()
					$.ajax(
						{
							url: 'https://morita.website/ir/code',
							type: 'POST',
							data:
							{
								'code': code
							}
						})
						.done(function (data)
						{
							console.log(data)
						})
				})
		IRCodeList
			.append(IRli)
	}
})