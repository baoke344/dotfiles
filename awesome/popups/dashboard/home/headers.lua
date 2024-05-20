--Standard Modules
local wibox = require("wibox")
local gears = require("gears")
local beautiful = require("beautiful")
local dpi = beautiful.xresources.apply_dpi

--Custom Modules
local color = require("popups.color")
local user = require("popups.user_profile")

-----------------------
--Header text----------
-----------------------
local create_header = function(text)
	local textbox = wibox.widget {
		markup = '<span color="' ..
				color.blueish_white .. '" font="Ubuntu Nerd Font bold 16">' .. text .. '</span>',
		font = "Ubuntu Nerd Font 14",
		widget = wibox.widget.textbox,
		fg = color.white
	}

	local header = wibox.widget {
		{
			{
				textbox,
				widget = wibox.container.margin,
				top = dpi(7),
				bottom = dpi(5),
				right = dpi(5),
				left = dpi(8),
			},
			widget = wibox.container.background,
			bg = color.background_lighter,
			shape = function(cr, width, height)
				gears.shape.rounded_rect(cr, width, height, 7)
			end,
		},
		widget = wibox.container.margin,
		top = dpi(14),
		left = dpi(12),
		right = dpi(12),
		forced_height = dpi(61),


	}

	return header
end

local headers = {
	home = create_header("  Hello " .. user.name),
	todo = create_header("  ToDo and Timer"),
	sys_monitor = create_header('  System monitor'),
	settings = create_header("  Settings")
}

return headers
