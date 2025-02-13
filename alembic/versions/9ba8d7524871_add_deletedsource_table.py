"""add deletedsource table

Revision ID: 9ba8d7524871
Revises: eff1387cfd0b
Create Date: 2022-03-15 12:25:59.145300

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "9ba8d7524871"
down_revision = "eff1387cfd0b"
branch_labels = None
depends_on = None


def upgrade():
    # ### Add DeletedSource table ###
    op.create_table(
        "deletedsource",
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.PrimaryKeyConstraint("uuid", name=op.f("pk_deletedsource")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### Remove DeletedSource table ###
    op.drop_table("deletedsource")
    # ### end Alembic commands ###
