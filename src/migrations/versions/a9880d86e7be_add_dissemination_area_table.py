"""add dissemination area table

Revision ID: a9880d86e7be
Revises: 05ccfb61e7da
Create Date: 2021-01-06 05:53:16.839314

"""
import sqlalchemy as sa
from alembic import op
from geoalchemy2 import Geometry

# revision identifiers, used by Alembic.
revision = "a9880d86e7be"
down_revision = "05ccfb61e7da"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "dissemination_area",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("dissemination_area_id", sa.String(length=8), nullable=True),
        sa.Column("province_id", sa.String(), nullable=True),
        sa.Column("province_name", sa.String(), nullable=True),
        sa.Column("census_division_id", sa.String(length=4), nullable=True),
        sa.Column("census_division_name", sa.String(length=100), nullable=True),
        sa.Column("census_division_type", sa.String(length=3), nullable=True),
        sa.Column(
            "census_consolidated_subdivision_id", sa.String(length=7), nullable=True
        ),
        sa.Column(
            "census_consolidated_subdivision_name", sa.String(length=100), nullable=True
        ),
        sa.Column("census_subdivision_id", sa.String(length=7), nullable=True),
        sa.Column("census_subdivision_name", sa.String(length=100), nullable=True),
        sa.Column("census_subdivision_type", sa.String(length=3), nullable=True),
        sa.Column("economic_region_id", sa.String(length=4), nullable=True),
        sa.Column("economic_region_name", sa.String(length=100), nullable=True),
        sa.Column(
            "statistical_area_classification_code", sa.String(length=4), nullable=True
        ),
        sa.Column(
            "statistical_area_classification_type", sa.String(length=1), nullable=True
        ),
        sa.Column("census_metro_area_id", sa.String(length=3), nullable=True),
        sa.Column("census_metro_area_province_id", sa.String(length=5), nullable=True),
        sa.Column("census_metro_area_name", sa.String(length=100), nullable=True),
        sa.Column("census_metro_area_type", sa.String(length=1), nullable=True),
        sa.Column("census_tract_id", sa.String(length=10), nullable=True),
        sa.Column("census_tract_name", sa.String(length=7), nullable=True),
        sa.Column(
            "aggregated_dissemination_area_id", sa.String(length=8), nullable=True
        ),
        sa.Column(
            "geometry",
            Geometry(from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("dissemination_area")
    # ### end Alembic commands ###
