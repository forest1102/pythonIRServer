$(function ()
{
	console.log('start jquery')
	$('#addIRCode')
		.on('submit', function (e)
		{
			e.preventDefault()
			console.log($('#name')
				.val())
			console.log('clicked ircode')
			$.ajax(
				{
					url: '/code-from' + $('#memo_no'),
				})
				.done(function (code)
				{
					console.log(code);
				})
			// .done(function (data)
			// {
			// 	console.log(d)
			// 	var IRli = $('<li><button type="button" class="btn btn-primary">' + d.name + '</button></li>')
			// 
			// 	$('button', IRli)
			// 		.click(
			// 			function (event)
			// 			{
			// 				event.preventDefault()
			// 				$.ajax(
			// 					{
			// 						url: '/code',
			// 						type: 'POST',
			// 						data:
			// 						{
			// 							'code': d.code
			// 						}
			// 					})
			// 					.done(function (data)
			// 					{
			// 						console.log(data)
			// 					})
			// 
			// 			})
			// 
			// 
			// 	$('#IRCodeList')
			// 		.append(IRli)
			// })
		})






})