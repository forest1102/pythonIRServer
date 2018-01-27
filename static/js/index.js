$(function ()
{
	console.log('start jquery')
	$('#getIRCode')
		.submit(function (e)
		{
			e.preventDefault()
			$.ajax('/code-from/' + $('#memo_no')
					.val())
				.done(function (d)
				{
					console.log(d);
				})
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
					url: '/addcode',
					type: 'POST',
					data:
					{
						'name': $('#name')
							.val(),
						'code': $('#code')
							.val()
					}
				})
				.done(function (d)
				{
					console.log(d)
					var IRli = $('<li><button type="button" class="btn btn-primary">' + d.name + '</button></li>')

					$('button', IRli)
						.click(
							function (event)
							{
								event.preventDefault()
								$.ajax(
									{
										url: '/code',
										type: 'POST',
										data:
										{
											'code': d.code
										}
									})
									.done(function (data)
									{
										console.log(data)
									})

							})


					$('#IRCodeList')
						.append(IRli)
				})
		})






})