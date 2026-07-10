"""이부장의 Weekly Insight Studio - Streamlit 진입점."""

import streamlit as st

from src.database import init_db
from src.services import branding_service, product_service
from src.ui import (
    dashboard,
    evidence_board,
    layout,
    preview_export,
    product_library,
    settings,
    source_inbox,
    strategy_editor,
    theme,
)

st.set_page_config(page_title="이부장의 Weekly Insight Studio", page_icon="📊", layout="wide")

init_db()
product_service.sync_catalog_from_csv()

_branding = branding_service.get_branding()
theme.inject(
    st,
    theme.resolve_tokens(
        {
            "primary": _branding.get("primary_color"),
            "accent": _branding.get("accent_color"),
            "font-family": _branding.get("font_family"),
        }
    ),
)

MENU_RENDERERS = {
    "Weekly Dashboard": dashboard.render,
    "Source Inbox": source_inbox.render,
    "Evidence Board": evidence_board.render,
    "Strategy Editor": strategy_editor.render,
    "Product Library": product_library.render,
    "Preview & Export": preview_export.render,
    "Settings": settings.render,
}


def main() -> None:
    selected_menu = layout.render_sidebar()
    MENU_RENDERERS[selected_menu]()


if __name__ == "__main__":
    main()
