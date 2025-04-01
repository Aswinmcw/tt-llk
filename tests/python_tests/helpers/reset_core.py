# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
from helpers.device import *
from ttexalens.device import ConfigurationRegisterDescription, TensixRegisterDescription
from ttexalens.context import Context
from ttexalens.util import TTException, DATA_TYPE, TensixDataFormat

unpack_registers = [
    # UNPACK TILE DESCRIPTOR SEC0
    "UNPACK_TILE_DESCRIPTOR0_in_data_format",
    "UNPACK_TILE_DESCRIPTOR0_uncompressed",
    "UNPACK_TILE_DESCRIPTOR0_reserved_0",
    "UNPACK_TILE_DESCRIPTOR0_blobs_per_xy_plane",
    "UNPACK_TILE_DESCRIPTOR0_reserved_1",
    "UNPACK_TILE_DESCRIPTOR0_x_dim",
    "UNPACK_TILE_DESCRIPTOR0_y_dim",
    "UNPACK_TILE_DESCRIPTOR0_z_dim",
    "UNPACK_TILE_DESCRIPTOR0_w_dim",
    "UNPACK_TILE_DESCRIPTOR0_blobs_y_start_lo",
    "UNPACK_TILE_DESCRIPTOR0_blobs_y_start_hi",
    "UNPACK_TILE_DESCRIPTOR0_digest_type",
    "UNPACK_TILE_DESCRIPTOR0_digest_size",
    # UNPACK TILE DESCRIPTOR SEC1
    "UNPACK_TILE_DESCRIPTOR1_in_data_format",
    "UNPACK_TILE_DESCRIPTOR1_uncompressed",
    "UNPACK_TILE_DESCRIPTOR1_reserved_0",
    "UNPACK_TILE_DESCRIPTOR1_blobs_per_xy_plane",
    "UNPACK_TILE_DESCRIPTOR1_reserved_1",
    "UNPACK_TILE_DESCRIPTOR1_x_dim",
    "UNPACK_TILE_DESCRIPTOR1_y_dim",
    "UNPACK_TILE_DESCRIPTOR1_z_dim",
    "UNPACK_TILE_DESCRIPTOR1_w_dim",
    "UNPACK_TILE_DESCRIPTOR1_blobs_y_start_lo",
    "UNPACK_TILE_DESCRIPTOR1_blobs_y_start_hi",
    "UNPACK_TILE_DESCRIPTOR1_digest_type",
    "UNPACK_TILE_DESCRIPTOR1_digest_size",
    # UNPACK CONFIG SEC 0
    "UNPACK_CONFIG0_out_data_format",
    "UNPACK_CONFIG0_throttle_mode",
    "UNPACK_CONFIG0_context_count",
    "UNPACK_CONFIG0_haloize_mode",
    "UNPACK_CONFIG0_tileize_mode",
    "UNPACK_CONFIG0_unpack_src_reg_set_upd",
    "UNPACK_CONFIG0_unpack_if_sel",
    "UNPACK_CONFIG0_upsample_rate",
    "UNPACK_CONFIG0_reserved_1",
    "UNPACK_CONFIG0_upsample_and_interleave",
    "UNPACK_CONFIG0_shift_amount",
    "UNPACK_CONFIG0_uncompress_cntx0_3",
    "UNPACK_CONFIG0_unpack_if_sel_cntx0_3",
    "UNPACK_CONFIG0_force_shared_exp",
    "UNPACK_CONFIG0_reserved_2",
    "UNPACK_CONFIG0_uncompress_cntx4_7",
    "UNPACK_CONFIG0_unpack_if_sel_cntx4_7",
    "UNPACK_CONFIG0_reserved_3",
    "UNPACK_CONFIG0_limit_addr",
    "UNPACK_CONFIG0_reserved_4",
    "UNPACK_CONFIG0_fifo_size",
    "UNPACK_CONFIG0_reserved_5",
    # UNPACK CONFIG SEC 1
    "UNPACK_CONFIG1_out_data_format",
    "UNPACK_CONFIG1_throttle_mode",
    "UNPACK_CONFIG1_context_count",
    "UNPACK_CONFIG1_haloize_mode",
    "UNPACK_CONFIG1_tileize_mode",
    "UNPACK_CONFIG1_unpack_src_reg_set_upd",
    "UNPACK_CONFIG1_unpack_if_sel",
    "UNPACK_CONFIG1_upsample_rate",
    "UNPACK_CONFIG1_reserved_1",
    "UNPACK_CONFIG1_upsample_and_interleave",
    "UNPACK_CONFIG1_shift_amount",
    "UNPACK_CONFIG1_uncompress_cntx0_3",
    "UNPACK_CONFIG1_unpack_if_sel_cntx0_3",
    "UNPACK_CONFIG1_force_shared_exp",
    "UNPACK_CONFIG1_reserved_2",
    "UNPACK_CONFIG1_uncompress_cntx4_7",
    "UNPACK_CONFIG1_unpack_if_sel_cntx4_7",
    "UNPACK_CONFIG1_reserved_3",
    "UNPACK_CONFIG1_limit_addr",
    "UNPACK_CONFIG1_reserved_4",
    "UNPACK_CONFIG1_fifo_size",
    "UNPACK_CONFIG1_reserved_5",
]

from ttexalens.debug_risc import RiscDebug, RiscLoc
from ttexalens.coordinate import OnChipCoordinate


def reset_unpack_registers(context: Context) -> None:
    for reg in unpack_registers:
        write_tensix_register("0,0", reg, 0, context=context)
