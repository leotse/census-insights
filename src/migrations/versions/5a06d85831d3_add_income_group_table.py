"""add income group table

Revision ID: 5a06d85831d3
Revises: 627d10c2ed63
Create Date: 2021-01-03 19:53:32.339538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5a06d85831d3"
down_revision = "627d10c2ed63"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "income_groups",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("geo_code", sa.String(), nullable=True),
        sa.Column("geo_name", sa.String(), nullable=True),
        sa.Column("geo_level", sa.Integer(), nullable=True),
        sa.Column("total", sa.Integer(), nullable=True),
        sa.Column("income_10k_to_20k", sa.Integer(), nullable=True),
        sa.Column("income_20k_to_30k", sa.Integer(), nullable=True),
        sa.Column("income_30k_to_40k", sa.Integer(), nullable=True),
        sa.Column("income_40k_to_50k", sa.Integer(), nullable=True),
        sa.Column("income_50k_to_60k", sa.Integer(), nullable=True),
        sa.Column("income_60k_to_70k", sa.Integer(), nullable=True),
        sa.Column("income_70k_to_80k", sa.Integer(), nullable=True),
        sa.Column("income_80k_to_90k", sa.Integer(), nullable=True),
        sa.Column("income_90k_to_100k", sa.Integer(), nullable=True),
        sa.Column("income_100k_to_150k", sa.Integer(), nullable=True),
        sa.Column("income_150k_plus", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_income_groups_geo_code"), "income_groups", ["geo_code"], unique=False
    )
    op.create_index(
        op.f("ix_income_groups_year"), "income_groups", ["year"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_income_groups_year"), table_name="income_groups")
    op.drop_index(op.f("ix_income_groups_geo_code"), table_name="income_groups")
    op.drop_table("income_groups")
    # ### end Alembic commands ###