# main.py
#
# Copyright 2025 AuthorName
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import gi
import sys

from gettext import gettext as _
from typing import Any, Callable, List, Optional

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gio, Gtk  # noqa: E402
from .window import TurturWindow  # noqa: E402


class TurturApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self) -> None:
        super().__init__(
            application_id="org.example.Turtur",
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
            resource_base_path="/org/example/Turtur",
        )
        self.create_action("quit", lambda *_: self.quit(), ["<primary>q"])
        self.create_action("about", self.on_about_action)
        self.create_action("preferences", self.on_preferences_action)

    def do_activate(self) -> None:
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = TurturWindow(application=self)
        win.present()

    def on_about_action(self, *args: Any) -> None:
        """Callback for the app.about action."""
        about = Adw.AboutDialog(
            application_name="turtur",
            application_icon="org.example.Turtur",
            developer_name="AuthorName",
            version="0.1.0",
            developers=["AuthorName"],
            copyright="© 2025 AuthorName",
        )
        # Translators: Replace "translator-credits" with your name/username, and optionally an email or URL.
        about.set_translator_credits(_("translator-credits"))
        about.present(self.props.active_window)

    def on_preferences_action(self, widget: Gtk.Widget, _: Any) -> None:
        """Callback for the app.preferences action."""
        print("app.preferences action activated")

    def create_action(
        self,
        name: str,
        callback: Callable[..., Any],
        shortcuts: Optional[List[str]] = None,
    ) -> None:
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version: str) -> int:
    """The application's entry point."""
    app = TurturApplication()
    return app.run(sys.argv)
